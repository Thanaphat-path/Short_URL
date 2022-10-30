# test function



# from dataclasses import field
# from unittest import result
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# # cluster = "mongodb+srv://admin:pxWmp2vgKiqMtjv1@cluster0.b6v1fml.mongodb.net/URL?retryWrites=true&w=majority"

# client = MongoClient("mongodb+srv://admin:pxWmp2vgKiqMtjv1@cluster0.b6v1fml.mongodb.net/URL?retryWrites=true&w=majority")
# db = client.URL
# todos =db.ShortURL
# # print(client.list_database_names())
# # print(db.list_collection_names())

# add =[{
#     "original_url":"https://www.google.com/",
#     "short_url":"https://www.google.com/one",
#     "count":1,
# }]

# def new_url_or_not(url):
#     results = todos.find({"original_url":str(url) })
#     for x in results:
#         if url == x["original_url"]:
#             return True
#     return False


# url="https://www.google.com/"
# def update_count(url):
#     results = todos.find({"original_url":url})
#     y=0
#     for x in results:
#         y=x["count"]
#         y=y+1
#     return y

# # result =todos.insert_many(add)
# # result = todos.delete_one({})
# # update_count(short_id)

# # if new_url_or_not(url):
# #     print(url)
#     # result = todos.update_one({"original_url":url},{"$set":{"count":update_count(url)}})

# # results = todos.find({})
# # print(results)
# # for result in results:
# #     print(result["original_url"])

# # results = todos.find({"short_url":short_id})
# # print(results)

# # for x in results:
# #     # print(x)
# #     if short_id == x["short_url"]:
# #         print ("TRUE")
# #     print ("False")


# import qrcode

# short_url="https://www.youtube.com"
# short_id="asdsad"
# QR =qrcode.make(short_url)
# # print(str_QR)
# QR.save("core/static/img_QR/"+short_id+".jpg")
