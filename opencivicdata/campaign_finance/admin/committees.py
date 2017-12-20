#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Committee-related models.
"""
from django.contrib import admin
from opencivicdata.core.admin import base
from .. import models


@admin.register(models.CommitteeType)
class CommitteeTypeAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the CommitteeType model.
    """
    readonly_fields = (
        "name",
        "id",
        "jurisdiction",
        "extras",
        "created_at",
        "updated_at",
    )
    list_display = (
        "name",
        "jurisdiction",
    )
    fields = readonly_fields
    search_fields = ("name",)
    list_filter = ("jurisdiction__name",)


class CommitteeIdentifierInline(base.IdentifierInline):
    """
    Custom inline administrative panely for CommitteeIdentifier model.
    """
    model = models.CommitteeIdentifier


class CommitteeSourceInline(base.ReadOnlyTabularInline):
    """
    Custom inline administrative panely for CommitteeSource model.
    """
    readonly_fields = ("url", "note")
    model = models.CommitteeSource


class CommitteeNameInline(base.ReadOnlyTabularInline):
    """
    Custom inline administrative panely for CommitteeName model.
    """
    readonly_fields = (
        'name',
        'note',
        'start_date',
        'end_date',
    )
    model = models.CommitteeName


class CommitteeStatusInline(base.ReadOnlyTabularInline):
    """
    Custom inline administrative panely for CommitteeStatus model.
    """
    readonly_fields = (
        "classification",
        "note",
        "start_date",
        "end_date"
    )
    model = models.CommitteeStatus


class CommitteeCandidacyDesignationInline(base.ReadOnlyTabularInline):
    """
    Custom inline administrative panely for CommitteeCandidacyDesignation model.
    """
    readonly_fields = (
        "candidacy",
        "designation",
    )
    model = models.CommitteeCandidacyDesignation


@admin.register(models.Committee)
class CommitteeAdmin(base.ModelAdmin):
    """
    Custom administrative panel for the Committee model.
    """
    readonly_fields = (
        "name",
        "id",
        "committee_type",
        "image",
        "parent",
        "ballot_measure_options_supported",
        "extras",
        "created_at",
        "updated_at",
    )
    list_display = (
        "name",
        "committee_type"
    )
    fields = readonly_fields
    search_fields = ("name",)
    list_filter = ("committee_type__name",)
    inlines = (
        CommitteeIdentifierInline,
        CommitteeNameInline,
        CommitteeStatusInline,
        CommitteeCandidacyDesignationInline,
        CommitteeSourceInline
    )
