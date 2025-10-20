from pyspark.sql import DataFrame
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType

class DataProcessingService:
    def get_valid_product_category_pairs(self, products_df, categories_df, relations_df):
        joined_with_products = relations_df.join(products_df, "product_name", "inner")
        joined_with_categories = joined_with_products.join(categories_df, "category_name", "inner")
        return joined_with_categories.select("product_name", "category_name").distinct()
    
    def get_products_without_categories(self, products_df, relations_df):
        products_with_categories = relations_df.select("product_name").distinct()
        products_without_cats = products_df.join(
            products_with_categories, "product_name", "left_anti"
        )
        return products_without_cats.withColumn("category_name", lit(None).cast(StringType()))
    
    def combine_results(self, pairs_df, no_category_df):
        return pairs_df.union(no_category_df)