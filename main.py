# coding: UTF-8
import hcl
import yaml
import re
import codecs


def tag_check_review(resource_dict, review_dict_list):
    for review_dict in review_dict_list:
        if "tags" not in resource_dict:
            return False, "tags not use"
        if review_dict["tag"]["key"] not in resource_dict["tags"]:
            return False, "need tag " + review_dict["tag"]["key"]
        if not re.match(review_dict["tag"]["regex"], resource_dict["tags"][review_dict["tag"]["key"]]):
            return False, "tag regex not matched " + review_dict["tag"]["key"] + " " + review_dict["tag"]["regex"]
        return True, "pass"


if __name__ == '__main__':
    with codecs.open('./s3.tf', 'r', 'utf-8') as fp:
        obj = hcl.load(fp)

    with codecs.open('./review_book/s3.yaml', 'r', 'utf-8') as fp2:
        review_book = yaml.load(fp2)

    for key in obj["resource"]["aws_s3_bucket"].keys():
        flg, res = tag_check_review(obj["resource"]["aws_s3_bucket"][key], review_book["aws_s3_bucket"])
        print(key)
        print(res)
