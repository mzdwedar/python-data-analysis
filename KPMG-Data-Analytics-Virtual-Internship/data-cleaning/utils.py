import pandas as pd
import numpy as np

def create_age(demo):
  demo['age'] = (2017 - pd.DatetimeIndex(demo.DOB.fillna(demo.DOB.mean())).year).astype(np.int8)
  return demo

def create_age_bins(demo):
  demo['age_bins']  = pd.cut(x=demo.age, bins=[10, 19, 29, 39, 49, 86])
  return demo

def clean_demo(demo):
  """
  clean customer_demographic
  """
  return (demo
  .drop(columns=['default'])

  .assign(
      gender = demo.gender.replace({'Femal':'F', 'Female':'F', 'Male':'M'}).astype('category'),
      wealth_segment = demo.wealth_segment.astype('category'),
      owns_car = demo.owns_car.replace({'Yes':1, 'No':0}).astype(np.int8),
      deceased_indicator = demo.deceased_indicator.replace({'N':0, 'Y':1}).astype(np.int8),
      job_title = demo.job_title.fillna(demo.job_title.mode().iloc[0]),
      tenure = demo.tenure.fillna(demo.tenure.mean()).astype(np.int8),
      job_industry_category = demo.job_industry_category.fillna(demo.job_industry_category.mode().iloc[0]).astype('category'),
      past_3_years_bike_related_purchases = demo.past_3_years_bike_related_purchases.fillna(demo.past_3_years_bike_related_purchases.mean()).astype(np.uint8),
      DOB = demo.DOB.fillna(demo.DOB.mean()),

    )
  
  .pipe(create_age)
  .pipe(create_age_bins)

  .drop(axis=0, index=33)
  .drop(columns=['DOB', 'age'])
  )


def clean_address(address):
  """
  clean address
  """
  return (address
  .drop(axis=0, index=[3996, 3997, 3998])
  .assign(
      state = address.state.replace({'New South Wales':'NSW', 'Victoria':'VIC'})
  )
  .astype({'customer_id':'int16', 'postcode':'int16', 'country':'category', 'property_valuation':'int8'})
  )

def clean_transactions(transactions):
  """
  clean transactions
  """
  return (transactions
  .drop(axis=0, index=[8707, 16700, 17468])
  .drop(columns=['product_first_sold_date'])
  .dropna()
  .astype({'transaction_id':'int16', 'customer_id':'int16', 'product_id':'int16', 'list_price':'float16', 'standard_cost':'float16', 'brand':'category',
            'product_line':'category', 'product_class':'category', 'product_size':'category', 'order_status':'category', 'online_order':'int8'})
  )