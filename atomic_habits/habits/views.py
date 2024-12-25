from rest_framework import generics
from habits.serializers import HabitSerializer
from habits.models import habit, IsOwnerOrReadOnly
from habits.paginators import habitPaginator
from habits.tasks import send_reminder


class HabiteListAPIView(generics.ListAPIView):
    """ Список привычек текущего пользователя с пагинацией """
    serializer_class = HabitSerializer
    pagination_class = habitPaginator

    def get_queryset(self):
        return habit.objects.filter(creator=self.request.user)


class HabitePublicListAPIView(generics.ListAPIView):
    """ Список публичных привычек """
    serializer_class = HabitSerializer
    pagination_class = habitPaginator
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        return habit.objects.filter(is_public=True)


class HabiteCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """
    queryset = habit.objects.all()
    serializer_class = HabitSerializer

class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = habit.objects.all()

class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = habit.objects.all()
