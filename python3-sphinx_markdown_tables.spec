Summary:	Sphinx extension for rendering tables written in markdown
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do renderowania tabel napisanych w markdownie
Name:		python3-sphinx_markdown_tables
Version:	0.0.17
Release:	2
License:	GPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-markdown-tables/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-markdown-tables/sphinx-markdown-tables-%{version}.tar.gz
# Source0-md5:	7240d3da2a215a462b849f66187b4ee7
URL:		https://pypi.org/project/sphinx-markdown-tables/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension for rendering tables written in markdown.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do renderowania tabel napisanych w markdownie.

%prep
%setup -q -n sphinx-markdown-tables-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/sphinx_markdown_tables
%{py3_sitescriptdir}/sphinx_markdown_tables-%{version}-py*.egg-info
