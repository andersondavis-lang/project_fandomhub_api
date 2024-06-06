"""Manager for Clubs App."""

from django.db.models import Manager


class ClubManager(Manager):
    """Manager for Club model."""

    def get_available(self):
        return self.filter(available=True)


class ClubMemberManager(Manager):
    """Manager for ClubMember model."""

    def get_available(self):
        return self.filter(available=True)

    def get_by_club(self, club):
        return self.get_available().filter(club=club).only("user", "joined_at")
