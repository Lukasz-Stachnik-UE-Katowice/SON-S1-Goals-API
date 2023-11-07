from uuid import uuid4
from app.routers.models.Comment import Comment
from app.routers.models.LinkedResource import LinkedResource
from app.routers.models.Goal import Goal

comment = Comment(user_id="26441ba4-ec61-472a-bf9a-3e6e1bc55020", date_time="01-01-1990", text="Dzien dobry")
comment2 = Comment(user_id="26441ba4-ec61-472a-bf9a-3e6e1bc55020", date_time="03-01-1990", text="Do widzenia")
linked = LinkedResource(title="Tytul1", url="Url example")
linked2 = LinkedResource(title="Tytul2", url="Url example2")
sample_goal = Goal(
    id='26441ba4-ec61-472a-bf9a-3e6e1bc55020',
    due_date='2023-12-31',
    frequency='weekly',
    comment=[comment, comment2],
    # comment=[,
    #          Comment(user_id="26441ba4-ec61-472a-bf9a-3e6e1bc55020", datetime="03-01-1990",
    #                  text="Jakies inne przywitanie")],
    progress=0.5,
    reminders=["Rob cos", "wstawaj"],
    notes=[],
    privacy="private",
    shared_with=["26441ba4-ec61-472a-bf9a-3e6e1bc55021"],
    tags=["#sila"],
    linked_resources=[linked,
                      linked2],    badges=["badge1", "badge2"]

)
sample_goal2 = Goal(
    id='26441ba4-ec61-472a-bf9a-3e6e1bc55021',
    due_date='2010-12-20',
    frequency='daily',
comment=[comment, comment2],
    # comment=[,
    #          Comment(user_id="26441ba4-ec61-472a-bf9a-3e6e1bc55020", datetime="03-01-1990",
    #                  text="Jakies inne przywitanie")],
    progress=0.5,
    reminders=["Rob cos", "wstawaj"],
    notes=[],
    privacy="private",
    shared_with=["26441ba4-ec61-472a-bf9a-3e6e1bc55021"],
    tags=["#sila"],
    linked_resources=[linked,
                      linked2],    badges=["badge1", "badge2"]
)
sample_goals = [sample_goal, sample_goal2]
