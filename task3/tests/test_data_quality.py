import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.testing import assertDataFrameEqual
from main import create_products_categories_dataframe

class TestDataQuality:
    def setup_method(self):
        self.spark = SparkSession.builder \
            .appName("test") \
            .master("local[2]") \
            .getOrCreate()

    def teardown_method(self):
        self.spark.stop()

    def test_invalid_relations_ignored(self):
        products_df = self.spark.createDataFrame([("valid_product",)], ["product_name"])
        categories_df = self.spark.createDataFrame([("valid_category",)], ["category_name"])
        relations_df = self.spark.createDataFrame([
            ("valid_product", "valid_category"),
            ("invalid_product", "valid_category"),
            ("valid_product", "invalid_category")
        ], ["product_name", "category_name"])
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_data = [("valid_product", "valid_category")]
        expected_df = self.spark.createDataFrame(expected_data, ["product_name", "category_name"])
        
        assertDataFrameEqual(result, expected_df)
    
    def test_duplicate_relations_handled(self):
        products_df = self.spark.createDataFrame([("product",)], ["product_name"])
        categories_df = self.spark.createDataFrame([("category",)], ["category_name"])
        relations_df = self.spark.createDataFrame([
            ("product", "category"),
            ("product", "category")
        ], ["product_name", "category_name"])
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_data = [("product", "category")]
        expected_df = self.spark.createDataFrame(expected_data, ["product_name", "category_name"])
        
        assertDataFrameEqual(result, expected_df)
        