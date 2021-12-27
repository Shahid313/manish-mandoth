from application import app
import os
from application.Apis.user import user
from application.Apis.product import product
from application.Apis.message import message
from flask import Blueprint

apis = Blueprint('apis', __name__,static_folder='../static')




# User part Starts from here


@apis.route('/sign_up',methods=['POST'])
def SignUp():
    return user.SignUp()

@apis.route('/sign_in',methods=['POST'])
def SignIn():
    return user.SignIn()


@apis.route('/profile')
def Profile():
    return user.Profile()
# User part Ends  here






#Product part Stars from here
@apis.route('/add_product',methods=['POST'])
def AddProduct():
    return product.AddProduct()


@apis.route('/get_all_products')
def GetAllProducts():
    return product.Index()



@apis.route('/search_product')
def SearchProduct():
    return product.SearchProduct()
    

@apis.route('/make_product_favorite',methods=['POST'])
def MakeProductFavorite():
    return product.MakeProductFavorite()


@apis.route('/get_all_my_favorite_product')
def GetAllMyFavoriteProducts():
    return product.MyFavoriteProducts()


@apis.route('/get_my_products')
def GetAllMyProducts():
    return product.MyProducts()


@apis.route('/view_product')
def ViewProduct():
    return product.ViewProduct()



@apis.route('/add_to_cart_product',methods=['POST'])
def AddToCartProduct():
    return product.AddToCartProduct()



@apis.route('/get_cart_products')
def GetCartProducts():
    return product.GetCartProducts()

@apis.route('/remove_product_from_cart')
def RemoveFromCartProduct():
    return product.RemoveFromCartProduct()



@apis.route('/place_order')
def PlaceOrder():
    return product.PlaceOrder()

@apis.route('/get_all_notifications')
def GetAllNotifications():
    return product.GetAllNotifications()

@apis.route('/delete_notification')
def DeleteNotification():
    return product.DeleteNotification()

@apis.route('/get_all_pending_orders_from_buyer')
def GetAllPendingOrdersFromBuyer():
    return product.GetAllPendingOrderFromBuyer()


@apis.route('/accept_order_from_buyer')
def AcceptOrderFromBuyer():
    return product.AcceptOrderFromBuyer()


@apis.route('/reject_order_from_buyer')
def RejectOrderFromBuyer():
    return product.RejectOrderFromBuyer()


@apis.route('/delete_placed_orders')
def DeletePlacedOrder():
    return product.DeletePlacedOrder()


@apis.route('/my_placed_orders')
def MyPlacedOrders():
    return product.MyPlacedOrders()   


#Product part End  here



# Messages Part Starts From here
@apis.route('/send_message',methods=['POST'])
def SendMessage():
    return message.SendMessage()


@apis.route('/get_messages',methods=['GET'])
def GetMessages():
    return message.GetMessages()

@apis.route('/get_recent_chats',methods=['GET'])
def GetRecentChats():
    return message.GetRecentChats()
