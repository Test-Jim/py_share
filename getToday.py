#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
from sqlalchemy import create_engine
import time

# Industry=ts.get_industry_classified()
# Concept=ts.get_concept_classified()
# MediumSmall=ts.get_sme_classified()
# Cyb=ts.get_gem_classified()
# Risk=ts.get_st_classified()
# hs300=ts.get_hs300s()
sz50=ts.get_sz50s()
print type(sz50)
# zz500=ts.get_zz500s()
# end=ts.get_terminated()
# pause=ts.get_suspended()
engine = create_engine('mysql://liaw:234589@183.134.75.126/test?charset=utf8')

# Industry.to_sql('Industry_Category',engine,if_exists='append')#行业分类if_exists='append'
# Concept.to_sql('Concept_Category',engine)#概念分类
# MediumSmall.to_sql('MediumSmall_Category',engine)#中小板分类
# Cyb.to_sql('Chuangyeban_Category',engine)#创业板分类
# Risk.to_sql('RishWaring_Category',engine)#风险警示板分类
# hs300.to_sql('hs300_Category',engine)#沪深300
# sz50.to_sql('sz50_Category',engine)#上证50分类
# zz500.to_sql('zz500_Category',engine)#中证500分类
# end.to_sql('end_Category',engine)#终止上市分类
# pause.to_sql('pause_Category',engine)#暂停上市



