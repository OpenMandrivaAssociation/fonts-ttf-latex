Summary:	LaTeX TrueType fonts for LyX
Name:		fonts-ttf-latex
Version:	0.1
Release:	24
# see README: these fonts were converted from the LaTeX .pfb forms,
#             and are under the respective licenses of the sources.
License:	Distributable
Group:		System/Fonts/True type
Url:		http://wiki.lyx.org/pmwiki.php/FAQ/Qt
Source0:	http://movementarian.org/latex-xft-fonts-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
Provides:	latex-xft-fonts

%description
This Package provides LaTeX TrueType fonts so that LyX can display LaTex
characters.

%prep
%setup -qn latex-xft-fonts-%{version}

%build
sed -i -e "s|INSTALLDIR=.*|INSTALLDIR=%{_datadir}/fonts/TTF/latex|" Makefile

%install
%makeinstall_std

(
cd %{buildroot}/%{_datadir}/fonts/TTF/latex/
# those are not unicode but in latex encoding
/usr/sbin/ttmkfdir -u | sed 's/iso10646-1/misc-fontspecific/' > fonts.scale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/latex \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-latex:pri=50

%files
%doc README
%dir %{_datadir}/fonts/TTF/latex/
%{_datadir}/fonts/TTF/latex/*.ttf
%config(noreplace) %{_datadir}/fonts/TTF/latex/fonts.dir
%config(noreplace) %{_datadir}/fonts/TTF/latex/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-latex:pri=50

