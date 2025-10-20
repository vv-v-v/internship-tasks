from services.product_category_service import ProductCategoryService

def create_products_categories_dataframe(products_df, categories_df, relations_df):
    return ProductCategoryService().create_products_categories_df(
        products_df, categories_df, relations_df
    )
