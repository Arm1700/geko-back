from rest_framework import serializers
from .models import Language, Category, Review, Event, PopularCourse, CategoryTranslation, PopularCourseTranslation, \
    ReviewTranslation, EventTranslation, LessonInfoTranslation, LessonInfo


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField()


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'name')


class CategoryTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = CategoryTranslation
        fields = ('language', 'text')


class PopularCourseTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = PopularCourseTranslation
        fields = ('language', 'lang', 'title', 'skill_level', 'assessments', 'desc', 'certification')


class EventTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = EventTranslation
        fields = ('language', 'title', 'description', 'place')


class ReviewTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = ReviewTranslation
        fields = ['language', 'comment']


class LessonInfoTranslationSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = LessonInfoTranslation
        fields = ['language', 'title']


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    translations = CategoryTranslationSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'image', 'translations', 'order')

    def get_image(self, obj):
        if obj.local_image:
            return obj.local_image.url
        elif obj.image_url:
            return obj.image_url
        return None

    def to_representation(self, instance):
        language_code = self.context.get('language_code', None)
        representation = super().to_representation(instance)

        if language_code:
            translation = next((t for t in representation['translations'] if t['language']['code'] == language_code),
                               None)
            representation['translation'] = translation
            representation.pop('translations')
        return representation


class PopularCourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    translations = PopularCourseTranslationSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = PopularCourse
        fields = ('id', 'category', 'image', 'lectures', 'quizzes', 'duration', 'students',  'translations')

    def get_image(self, obj):
        if obj.local_image:
            return obj.local_image.url
        elif obj.image_url:
            return obj.image_url
        return None

    def to_representation(self, instance):
        language_code = self.context.get('language_code', None)
        representation = super().to_representation(instance)

        if language_code:
            translation = next((t for t in representation['translations'] if t['language']['code'] == language_code),
                               None)
            representation['translation'] = translation
            representation.pop('translations')
        return representation


class EventSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    translations = EventTranslationSerializer(many=True)
    available_slots = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = (
            'id', 'day', 'month', 'hour', 'image', 'status', 'total_slots', 'booked_slots',  'available_slots',
            'translations')

    def get_image(self, obj):
        if obj.local_image:
            return obj.local_image.url
        elif obj.image_url:
            return obj.image_url
        return None

    def to_representation(self, instance):
        language_code = self.context.get('language_code', None)
        representation = super().to_representation(instance)

        if language_code:
            translation = next((t for t in representation['translations'] if t['language']['code'] == language_code),
                               None)
            representation['translation'] = translation
            representation.pop('translations')
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    translations = ReviewTranslationSerializer(many=True)

    class Meta:
        model = Review
        fields = ['id', 'image', 'name', 'translations']

    def get_image(self, obj):
        if obj.local_image:
            return obj.local_image.url
        elif obj.image_url:
            return obj.image_url
        return None

    def to_representation(self, instance):
        language_code = self.context.get('language_code', None)
        representation = super().to_representation(instance)

        if language_code:
            translation = next((t for t in representation['translations'] if t['language']['code'] == language_code),
                               None)
            representation['translation'] = translation
            representation.pop('translations')
        return representation


class LessonInfoSerializer(serializers.ModelSerializer):
    translations = LessonInfoTranslationSerializer(many=True, read_only=True)
    icon = serializers.CharField()

    class Meta:
        model = LessonInfo
        fields = ['id', 'icon', 'count', 'translations']

    def to_representation(self, instance):
        language_code = self.context.get('language_code', None)
        representation = super().to_representation(instance)

        if language_code:
            translation = next(
                (t for t in representation['translations'] if t['language']['code'] == language_code),
                None)
            representation['translation'] = translation
            representation.pop('translations')
        return representation
