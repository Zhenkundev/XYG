from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# from backend.base.models import UserProfile
from .models import Order, Review, Trainer, Trainee


class UserSerializerWithTrainee(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    trainee = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'first_name', 'last_name', 'isAdmin', 'trainee']

    def get_user_id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name + ' ' + obj.last_name
        if name == '':
            name = obj.email

        return name

    def get_trainee(self, obj):
        serializer = TraineeSerializer(obj.trainee, many=False)
        return serializer.data


class UserSerializerWithTrainer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    trainer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'first_name', 'last_name', 'isAdmin', 'trainer']

    def get_user_id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name + ' ' + obj.last_name
        if name == '':
            name = obj.email

        return name

    def get_trainer(self, obj):
        serializer = TrainerSerializer(obj.trainer, many=False)
        return serializer.data


class UserSerializerWithToken(UserSerializerWithTrainee, UserSerializerWithTrainer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'first_name', 'last_name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Trainer
        fields = '__all__'

    def get_reviews(self, obj):
        # TODO review
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    trainee = serializers.SerializerMethodField(read_only=True)
    trainer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_trainee(self, obj):
        trainee = obj.trainee
        serializer = TraineeSerializer(trainee, many=False)
        return serializer.data

    def get_trainer(self, obj):
        trainer = obj.trainer
        serializer = TrainerSerializer(trainer, many=False)
        return serializer.data