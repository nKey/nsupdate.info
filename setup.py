"""
setup for nsupdate package
"""

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme_content = f.read()

setup(
    name='nsupdate',
    use_scm_version=True,
    url='http://github.com/nsupdate-info/nsupdate.info/',
    license='BSD',
    author='The nsupdate.info Team (see AUTHORS)',
    author_email='info@nsupdate.info',
    description='A dynamic DNS update service',
    long_description=readme_content,
    keywords="dyndns ddns dynamic dns django",
    packages=find_packages('src', exclude=['_tests', ]),
    package_dir={'': 'src'},
    package_data={
        'nsupdate': [
            'templates/*.html',
            'templates/includes/*.html',
            'static/*.html',
            'static/*.png',
            'static/css/*.css',
            'locale/*/LC_MESSAGES/*',
        ],
        'nsupdate.accounts': [
            'templates/accounts/*.html',
            'templates/registration/*.html',
            'templates/registration/*.txt',
        ],
        'nsupdate.login': [
            'templates/*.html',
        ],
        'nsupdate.main': [
            'templates/main/*.html',
            'templates/main/includes/*.html',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    setup_requires=['setuptools_scm'],
    install_requires=[
        'dnspython<1.17.0',  # 1.16 is last with py27 support
        'netaddr',
        'django',
        'django-bootstrap-form',
        'django-registration-redux',
        'django-extensions',
        'social-auth-app-django',
        'requests',  # for our ddns_client
        'setuptools_scm'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: Name Service (DNS)',
    ],
)
