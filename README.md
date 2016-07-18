# JSS-Scripts

This repository contains scripts and documentation for managing our JSS.

## Basic JSS Structure

Our JSS is structured according to the following rules:

Everyone who is assigned a device has a User object in the JSS. Users have two Extension Attributes: Graduation Year and Role. Graduation Year is used to (mostly) uniquely identify age-based cohorts. Role is either "Staff" or "Student" and this is used to target configuration profiles at staff or students respectively

The JSS has a number of Smart Groups based on year of graduation. There is a smart group for each possible value in year of graduation.

In any year, individual groups of users in a specific class are formed by creating additional smart groups. These groups may be as simple as "Graduation Year is 2023", in which case there is a 1:1 correspondance between Class-of groups and actual classes. In other cases - particularly primary - composite classes may be created that union more than one Class-of group.

## Configuration Profile Scoping

There are three kinds of Configuration Profile scopes:

* Universal Profiles
* Conditional Profiles
* User-scoped Profiles

Universal Profiles are scoped to all (student) iPads unconditionally. Conditional Profiles are scoped to certain groups of devices based on certain conditions expressed in Smart Groups.

User-scoped profiles are scoped to users rather than to devices. This ensures that unconfigured devices still have the appropriate security profiles applied without any personal information - such as email addresses - being on the device.