import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.testing import assertDataFrameEqual
from main import create_products_categories_dataframe

class TestProductCategoryService:
    def setup_method(self):
        self.spark = SparkSession.builder \
            .appName("test") \
            .master("local[2]") \
            .getOrCreate()

    def teardown_method(self):
        self.spark.stop()

    def test_basic_functionality(self):
        products_data = [("product1",), ("product2",), ("product3",), ("product4",)]
        products_df = self.spark.createDataFrame(products_data, ["product_name"])
        
        categories_data = [("category1",), ("category2",), ("category3",)]
        categories_df = self.spark.createDataFrame(categories_data, ["category_name"])
        
        relations_data = [
            ("product1", "category1"), 
            ("product1", "category2"), 
            ("product2", "category1"), 
            ("product3", "category3")
        ]
        relations_df = self.spark.createDataFrame(relations_data, ["product_name", "category_name"])
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        expected_data = [
            ("product1", "category1"),
            ("product1", "category2"),
            ("product2", "category1"), 
            ("product3", "category3"),
            ("product4", None)
        ]
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)
        
        assertDataFrameEqual(result, expected_df)

    def test_products_with_multiple_categories(self):
        products_df = self.spark.createDataFrame([("laptop",), ("mouse",)], ["product_name"])
        categories_df = self.spark.createDataFrame([("electronics",), ("computers",)], ["category_name"])
        relations_df = self.spark.createDataFrame([
            ("laptop", "electronics"),
            ("laptop", "computers"),
            ("mouse", "electronics")
        ], ["product_name", "category_name"])
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        expected_data = [
            ("laptop", "electronics"),
            ("laptop", "computers"),
            ("mouse", "electronics")
        ]
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)
        
        assertDataFrameEqual(result, expected_df)