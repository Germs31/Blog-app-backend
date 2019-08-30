import models 

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

blog = Blueprint('blogs', 'blog', url_prefix='/blog/v1')

##################################################################################


@blog.route('/', methods=["GET"])
def get_all_blogs():
    try:
        blogs = [model_to_dict(blog) for blog in models.Blog.select()]
        return jsonify(data=blogs, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "there was a error getting the resource"})

##################################################################################


@blog.route('/', methods=["POST"])
def create_blogs():
    payload = request.get_json(force=True)

    blog = models.Blog.create(**payload)
    blog.created_by_id = 1
    blog_dict = model_to_dict(blog)

    return jsonify(data=blog_dict, status={"code": 201, "message": "success"})

##################################################################################


@blog.route('/<id>', methods=["GET"])
def get_one_blog(id):
    blog = models.Blog.get_by_id(id)

    return jsonify(data=model_to_dict(blog), status={"code": 200, "message": "success"})

##################################################################################


@blog.route('/<id>', methods=["PUT"])
def update_blog(id):
    payload = request.get_json(force=True)
    print(payload, 'it the payload')
    query = models.Blog.update(**payload).where(models.Blog.id == id)
    query.execute()

    updated_blog = models.Blog.get_by_id(id)

    return jsonify(data=model_to_dict(updated_blog), status={"code": 200, "message": "success"})

##################################################################################


@blog.route('/<id>', methods=["DELETE"])
def delete_blog(id):
    query = models.Blog.delete().where(models.Blog.id == id)
    query.execute()
    return jsonify(data='resources successfully deleted', status={"code": 200, "message": "resource deleted"}) 



