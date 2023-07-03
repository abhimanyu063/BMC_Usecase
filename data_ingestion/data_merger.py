from data_ingestion import data_loader

class DataMerger:
    def __init__(self):
        json_data = data_loader.Data_Getter('')
        self.customer_transaction_info = json_data.json_load('data/customer_transaction_info.json')
        self.customers_info = json_data.json_load('data/customers_info.json')
        self.orders_returned_info = json_data.json_load('data/orders_returned_info.json')
        self.product_info = json_data.json_load('data/product_info.json')
        self.region_seller_info = json_data.json_load('data/region_seller_info.json')
        

    def dataframe_merger(self):
        try:
            # Merging all dataframe into on dataframe.
            df = self.customer_transaction_info.merge(self.customers_info, on ='Customer ID', how= 'left')
            new_df = df.merge(self.orders_returned_info, on='Order ID', how= 'left')
            final_df = new_df.merge(self.product_info, on = 'Product ID', how= 'left')

            # Filtering data based on printer and Machines
            filter_df = final_df[(final_df['Product Name'].str.contains('Printer')) & (final_df['Sub-Category'] == 'Machines')]
            return filter_df

        except Exception as ex:
            print('error', ex)