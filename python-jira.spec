%global modname jira
%global distname jira-python
%global eggname jira_python

Name:               python-jira
Version:            0.13
Release:            2%{?dist}
Summary:            A library to ease use of the JIRA 5 REST APIs.

Group:              Development/Libraries
License:            BSD
URL:                http://pypi.python.org/pypi/jira-python
Source0:            http://pypi.python.org/packages/source/j/%{distname}/%{distname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-setuptools

BuildRequires:      python-requests
BuildRequires:      python-requests-oauthlib
BuildRequires:      python-tlslite
BuildRequires:      python-magic
BuildRequires:      ipython

Requires:           python-requests
Requires:           python-requests-oauthlib
Requires:           python-tlslite
Requires:           python-magic
Requires:           ipython

%description
A library to ease use of the JIRA 5 REST APIs.

%prep
%setup -q -n %{distname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

# Why does it even install these?  A mistake.
rm -rf %{buildroot}%{python2_sitelib}/tests/
rm -rf %{buildroot}%{python2_sitelib}/tools/


# The tests could be run with nosetests, but they require hardcoded
# certificates found on the author's computer.
#%%check
#nosetests

%files
# Filed an issue asking for license full text
# https://bitbucket.org/bspeakmon/jira-python/issue/70
%doc PKG-INFO
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{eggname}-%{version}*
%{_bindir}/jirashell


%changelog
* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.13-2
- Modernize python2 rpm macros.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.13-1
- Initial package for Fedora
