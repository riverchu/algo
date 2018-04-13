#!/usr/bin/env python3
# coding=utf-8

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        #判断是基类model还是要操作的实例类
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        #将属性中属于field类型的可写入数据库的类型取出
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        #记录在mapping中之后将原本类中的属性删除 否则会出现冲突 创建实例得到的值会被覆盖
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    #初始化方法 将对应子类进行dict类型的初始化
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    #设置返回对应元素
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    #不知道干啥用的
    def __setattr__(self, key, value):
        self[key] = value

    #保存如数据库的操作
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():#从mapping中依次去除对象获取对应值
            fields.append(v.name)
            params.append(getattr(self,k,None))
            #args.append(getattr(self, k, None))
        #将数据插入sql
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), str(params))
        print('SQL: %s' % sql)
        #print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
