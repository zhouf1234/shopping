from django.db import models

# Create your models here.

#用户表
class UserInfo(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upassword = models.CharField('密码',max_length=200,null=False)
    email = models.CharField('邮箱',max_length=50,null=True)
    phone = models.CharField('手机号',max_length=20,null=False)
    time = models.DateTimeField('注册时间',auto_now=True)
    isban = models.BooleanField('是否禁用',default=False)
    isdelete = models.BooleanField('是否删除',default=False)  #如果是，就是不可用了

#用户信息和地址表
class Adress(models.Model):
    aname = models.CharField('收货人',max_length=50,null=False)
    ads = models.CharField('收货地址',max_length=300,null=False)
    phone = models.CharField('收货电话',max_length=20,null=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

#商品分类表
class GoodsType(models.Model):
    title = models.CharField('分类名称',max_length=30)
    desc = models.CharField('分类描述',max_length=200,default='商品描述')
    isdelete = models.BooleanField('是否删除',default=False)

#商品信息表
class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    desc = models.CharField('描述', max_length=200)
    unit = models.CharField('单位',max_length=30)
    picture = models.ImageField('商品图片',upload_to='media')
    detail = models.CharField('商品详情',max_length=255,default='商品详情')
    isdelete = models.BooleanField('是否删除',default=False)
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)


#购物车表
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo,db_column='user_id',on_delete=models.CASCADE)
    good = models.ForeignKey(Goods,db_column='good_id',on_delete=models.CASCADE)
    ccount = models.IntegerField('数量',db_column='cart_count')

#订单表
class Order(models.Model):
    ORDERSTATUS = (
        (1, '未支付',),
        (2, '已支付',),
        (3, '订单取消',),
    )
    orderNo = models.CharField('商品编号',max_length=50)
    orderdetail = models.TextField('订单详情')
    adsname = models.CharField('收件人姓名',max_length=30,null=False)
    adsphone = models.CharField('收件人电话',max_length=20,null=False)
    ads = models.CharField('地址',max_length=300)
    time = models.DateTimeField(auto_now=True)
    acot = models.IntegerField('总数')
    acount = models.DecimalField('总价',max_digits=8,decimal_places=2)
    orderstatus = models.IntegerField('订单',choices=ORDERSTATUS,default=1)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)





