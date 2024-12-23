from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_message_about_habit():
    """Посылает за 5 минут до начала времени выполнения привычки напоминание"""
    now = datetime.now()
    current_weekday = now.isoweekday()
    habits = Habit.objects.filter(weekdays__number=current_weekday)

    for habit in habits:
        habit_time = habit.time
        habit_datetime = datetime.combine(datetime.today(), habit_time)

        if habit_datetime - timedelta(minutes=5) <= now <= habit_datetime:
            tg_chat_id = habit.owner.tg_chat_id
            message = f"Я буду {habit.action} в это время: {habit.time} в этом месте: {habit.location}"
            try:
                send_telegram_message(chat_id=tg_chat_id, message=message)
            except Exception as e:
                print(f"Ошибка отправки сообщения в Telegram: {e}")
