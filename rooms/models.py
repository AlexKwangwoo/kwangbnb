from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):  # db에 값 안줄꺼임
    # 이클래스는 이름을 입력할수있는 기능을 가지고있고 밑에 roomType 등등이
    # 이클래스를 상속받아서 이름을 입력할수있게 해줄수있다.
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):  # abstractItem이 들어가는 집합체라고 생각하자
    """ RoomType model Definition"""

    class Meta:
        verbose_name = "Room type"  # House room 인걸 룸을 대문자로 바꿔줌! 걍 이름변경
        # ordering = ["name"] 순서 정렬!


class Amenity(AbstractItem):
    """ Amenity model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"
        # 장고가 마음대로 aminitys라해서 이름 변경하는것!


class Facility(AbstractItem):
    """ Facility model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"
        # 장고가 마음대로 aminitys라해서 이름 변경하는것!
        # verbose_name 쓰면 ss가 두개 붙는다!


class HouseRule(AbstractItem):
    """ HouseRule model Definition"""

    class Meta:
        verbose_name = "House Rule"  # House room 인걸 룸을 대문자로 바꿔줌!


class Photo(core_models.TimeStampedModel):
    """ Photo model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
    # 룸한테 내목숨을 맡김... 룸사라지면 사진도 사라짐.

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 시간만 나온다.. dateTimeField랑 다름
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # host는 user랑 연결되어있어서
    # foreignKey를 사용해서 연결해줘야한다! room은 하나의 유저만 가질수있다
    # ondelete는 one to many만 가질수있따 foreign 키 있을때
    # related_name은 user가 찾을때 사용한다 즉 room_set.all() 입력대신
    # rooms.all() 을 입력할수있다

    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # 룸은 다양한 타입의 방을 가질수있다 many to many-> 강의가 바뀜 그냥 예시든거임
    # 룸을 하나의 객실타입만 가지고 싶게 했기때문에 foreignKey로 전환!
    # setnull 통해 orphan (고아)로 엄마 아빠랑 관계 없게 끊어버림

    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        # room object(1)이라고 나오는걸 사용자가 만든방 원래 이름으로 바꾸기
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return round(all_ratings / len(all_reviews), 2)
        # 여기서 reviews는 reviews패키지안의
        # models 파일속으 rooms 속의 related_name="reviews" <- 이것이다