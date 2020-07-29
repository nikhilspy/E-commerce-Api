Some features use sending of primary keys over the links that were not originally specified in the hackathon pdf
these are:
     changePassword
     deleteUser
     deleteProduct

So to run them correctly you need to specify the id of the object you want to edit
like:
    changePassword/(id)
    deleteUser/(id)

Also the user product list displays the id of the products added
superuser account
username = nikhil
password = nikhil0987


Working url routes:


path('platform/users', user_list_api, name = 'all-users'),
    path('platform/signup', user_create_api, name = 'sign-up'),
    path('platform/changePassword/<int:pk>', change_password_api, name= 'change-password' ),
    path('platform/login', login_user_api, name='login'),
    path('platform/deleteUser/<int:pk>', delete_user, name = 'delete-user'),
    path('platform/<int:pk>/products',view_product_list, name='list-products')


 path("pts/products", list_all_products, name='all-items' ),
    path("pts/products/create", create_product, name='create-item' ),
    path('pts/products/<int:pk>', view_product, name='view-product' ),
    path('pts/products/purchase', purchase_product, name='add-prod'),
    path('pts/products/review', add_review, name='add-review'),
    path('pts/products/<int:pk>/reviews', get_all_review, name='all-review'),
    path('pts/deleteProduct/<int:pk>', delete_product, name = 'del-product'),
    path('pts/products/rate', rate_product, name = 'rate'),

where substitue <int:pk> for orimary key or the id of the user or the product.