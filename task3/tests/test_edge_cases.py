import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.testing import assertDataFrameEqual
from main import create_products_categories_dataframe

class TestEdgeCases:
    def setup_method(self):
        self.spark = SparkSession.builder \
            .appName("test") \
            .master("local[2]") \
            .getOrCreate()

    def teardown_method(self):
        self.spark.stop()

    def test_no_products(self):
        schema = StructType([StructField("product_name", StringType(), True)])
        products_df = self.spark.createDataFrame([], schema)
        
        categories_df = self.spark.createDataFrame([("cat1",)], ["category_name"])
        
        rel_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        relations_df = self.spark.createDataFrame([], rel_schema)
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        expected_df = self.spark.createDataFrame([], expected_schema)
        
        assertDataFrameEqual(result, expected_df)
    
    def test_all_products_without_categories(self):
        products_df = self.spark.createDataFrame([("p1",), ("p2",)], ["product_name"])
        categories_df = self.spark.createDataFrame([("cat1",)], ["category_name"])
        
        rel_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        relations_df = self.spark.createDataFrame([], rel_schema)
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        expected_data = [("p1", None), ("p2", None)]
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)
        
        assertDataFrameEqual(result, expected_df)
    
    def test_no_categories(self):
        products_df = self.spark.createDataFrame([("p1",), ("p2",)], ["product_name"])
        
        schema = StructType([StructField("category_name", StringType(), True)])
        categories_df = self.spark.createDataFrame([], schema)
        
        rel_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        relations_df = self.spark.createDataFrame([], rel_schema)
        
        result = create_products_categories_dataframe(products_df, categories_df, relations_df)
        
        expected_schema = StructType([
            StructField("product_name", StringType(), True),
            StructField("category_name", StringType(), True)
        ])
        expected_data = [("p1", None), ("p2", None)]
        expected_df = self.spark.createDataFrame(expected_data, expected_schema)
        
        assertDataFrameEqual(result, expected_df)