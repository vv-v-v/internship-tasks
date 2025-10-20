from pyspark.sql import DataFrame
from .data_processing_service import DataProcessingService

class ProductCategoryService:
    def __init__(self):
        self.data_processor = DataProcessingService()
    
    def create_products_categories_df(self, products_df, categories_df, relations_df):
        pairs = self.data_processor.get_valid_product_category_pairs(
            products_df, categories_df, relations_df
        )
        no_category_products = self.data_processor.get_products_without_categories(
            products_df, relations_df
        )
        return self.data_processor.combine_results(pairs, no_category_products)
    