# coding: UTF-8
import hcl
import yaml
import codecs

with codecs.open('./s3.tf', 'r', 'utf-8') as fp:
    obj = hcl.load(fp)
    print(obj)

with codecs.open('./review_book/s3.yaml', 'r', 'utf-8') as fp2:
    review_book = yaml.load(fp2)
    print(review_book)
