# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!--
## [Unreleased]
-->

## [0.4.0] - 2019-11-13
### Added
- `Faker` scrubber now supports passing arbitrary arguments to faker providers and also non-text fields (thanks [Benedikt Bauer](https://github.com/mastacheata) and [Ronny Vedrilla](https://github.com/GitRon))

## [0.3.1] - 2018-09-10
### Fixed
- [#9](https://github.com/RegioHelden/django-scrubber/pull/9) `Hash` scrubber choking on fields with `max_length=None` - Thanks to [Charlie Denton](https://github.com/meshy)

## [0.3.0] - 2018-09-06
### Added
- Finally added some basic tests (thanks [Marco De Felice](https://github.com/md-f))
- `Hash` scrubber can now also be used on sqlite

### Changed
- **BREAKING**: scrubbers that are lazily initialized now receive `Field` instances as parameters, instead of field
  names. If you have custom scrubbers depending on the previous behavior, these should be updated. Accessing the
  field's name from the object instance is trivial: `field_instance.name`. E.g.: if you have `some_field = MyCustomScrubber`
  in any of your models' `Scrubbers`, this class must accept a `Field` instance as first parameter.
  Note that explicitly intializing any of the built-in scrubbers with field names is still supported, so if you were
  just using built-in scrubbers, you should not be affected by this change.
- related to the above, `FuncField` derived classes can now do connection-based setup by implementing the
  `connection_setup` method. This is mostly useful for doing different things based on the DB vendor, and is used to
  implement `MD5()` on sqlite (see added feature above)
- Ignore proxy models when scrubbing (thanks [Marco De Felice](https://github.com/md-f))
- Expand tests to include python 3.7 and django 2.1

## [0.2.1] - 2018-08-14
### Added
- Option to scrub only one model from the management command
- Support loading additional faker providers by config setting SCRUBBER\_ADDITIONAL\_FAKER\_PROVIDERS

### Changed
- Switched changelog format to the one proposed on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

## [0.2.0] - 2018-08-13
### Added
- scrubbers.Concat to make simple concatenation of scrubbers possible

## [0.1.4] - 2018-08-13
### Changed
- Make our README look beautiful on PyPI

## [0.1.3] - 2018-08-13
### Fixed
- [#1](https://github.com/RegioHelden/django-scrubber/pull/1) badly timed import - Thanks to [Charlie Denton](https://github.com/meshy)

## [0.1.2] - 2018-06-22
### Changed
- Use bumpversion and travis to make new releases
- rename project: django\_scrubber → django-scrubber

## [0.1.0] - 2018-06-22
### Added
- Initial release
