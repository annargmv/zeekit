# zeekit
Hey Dror :)
You need to login in order to use the API

```
username: dror
password: zeekit
```

In order to tun this project please install requirements

```pip install -r requierments.txt ```

Run this command for installing Postgres via docker 

```docker-compose -f docker-compose.services.yml up -d```

DB setup

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

Run the app by running the `main()` in `app.py` or `flask run`

##Routs in the system
Run the command `flask routes` in order to see the all possible routes

```
Endpoint                              Methods  Rule
------------------------------------  -------  -----------------------------------------
blogpost_api.get_blog_post_by_filter  GET      /blogpost/filter/<param>/<limit>/<offset>
blogpost_api.get_blog_post_by_filter  GET      /blogpost/filter/<param>
blogpost_api.get_blogpost             GET      /blogpost/blogpost
blogpost_api.get_blogpost             GET      /blogpost/blogpost/<limit>/<offset>
blogpost_api.get_blogpost_by_id       GET      /blogpost/<int:blog_id>
index                                 GET      /login
products_api.get_product_by_id        GET      /product/<int:product_id>
products_api.get_products             GET      /product/products
products_api.get_products             GET      /product/products/<limit>/<offset>
products_api.get_products_by_filter   GET      /product/filter/<param>/<limit>/<offset>
products_api.get_products_by_filter   GET      /product/filter/<param>
```


