from rest_framework import serializers
from surveys.models import Test, Answer, Choice, Question

class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    test = serializers.SlugRelatedField(queryset=Test.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    choice_text = serializers.CharField(max_length=200)

    class Meta:
        model = Answer
        filds = '__all__'
    
    def create(self, data):
        return Answer.objects.create(**data)

    def update(self, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).question_type
        try:
            if question_type == "one" or question_type == "text":
                obj = Answer.objects.get(question=attrs['question'].id, test=attrs['test'], user_id=attrs['user_id'])
            elif question_type == "multiple":
                obj = Answer.objects.get(question=attrs['question'].id, test=attrs['test'], user_id=attrs['user_id'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Already responded')



class ChoiceSerializer(serializers.Serializer): 
    id = serializers.IntegerField()
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=200)


    class Meta:
        model = Choice
        filds = '__all__'

    def create(self, data):
        return Choice.objects.create(**data)

    def update(self, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, choice_text=attrs['choice_text'])
        except Choice.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Choice already exists')


class QuestionSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    test = serializers.SlugRelatedField(queryset=Test.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=200)
    question_type = serializers.CharField(max_length=200)
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        filds = '__all__'

    def create(self, data):
        return Question.objects.create(**data)

    def update(self, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TestSerializer(serializers.Serializer): 
    test_name = serializers.CharField(max_length=100)
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    test_description = serializers.CharField()
    questions = QuestionSerializer(many=True, read_only=True)


    class Meta:
        model = Test
        filds = '__all__'
    
    def create(self, data):
        return Test.objects.create(**data)

    def update(self, data):
        if 'date_start' in data:
            raise serializers.ValidationError({'date_start': 'You must not change this field.'})
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance