from django.db import models


class user(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    username = models.CharField(max_length=30)


class tryout(models.Model):
    name = models.CharField(max_length=30)


class criterion(models.Model):
    tryoutID = models.ForeignKey(tryout, on_delete=models.CASCADE, related_name="eval_criteria")
    criteriaName = models.CharField(max_length=30)


class player(models.Model):
    tryoutID = models.ForeignKey(tryout, on_delete=models.CASCADE, related_name="players")
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)


class evalution(models.Model):
    playerID = models.ForeignKey(player, on_delete=models.CASCADE, related_name="evaluations")
    criterionID = models.ForeignKey(criterion, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()


class comment(models.Model):
    playerID = models.ForeignKey(player, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)


class team(models.Model):
    tryoutID = models.ForeignKey(tryout, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=30)


class session(models.Model):
    tryoutID = models.ForeignKey(tryout, on_delete=models.CASCADE, related_name="sessions")
    plan = models.FileField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
