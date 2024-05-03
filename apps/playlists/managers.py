"""Managers for Playlists App."""

from django.db.models import Manager


class PlaylistManager(Manager):
    """Manager for Author model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available playlists"""
        return self.get_queryset().filter(available=True)


class PlaylistBaseManager(Manager):
    """Manager for PlaylistBase."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available playlist items (Base)."""
        return self.get_queryset().filter(available=True)
