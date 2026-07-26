%define upstream_name    Pod-Loom
Name:		perl-%{upstream_name}
Version:	0.08
Release:	5

Summary:	Do-nothing template for Pod::Loom

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/madsen/pod-loom
Source0:	https://cpan.metacpan.org/authors/id/C/CJ/CJM/Pod-Loom-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Moose)
BuildRequires:	perl(PPI)
BuildRequires:	perl(Pod::Eventual)
BuildRequires:	perl(String::RewritePrefix)
BuildArch:	noarch

%description
Pod::Loom extracts all the POD sections from Perl code, passes the POD to a
template that may reformat it in various ways, and then returns a copy of
the code with the reformatted POD at the end.

A template may convert non-standard POD commands like '=method' and '=attr'
into standard POD, reorder sections, and generally do whatever it likes to
the POD.

The document being reformatted can specify the template to use with a line
like this:

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# %check
# %make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


