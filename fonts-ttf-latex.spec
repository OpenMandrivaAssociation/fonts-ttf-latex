
Summary:	LaTeX TrueType fonts for LyX
Name:		fonts-ttf-latex
Version:	0.1
Release:	%mkrel 4

# see README: these fonts were converted from the LaTeX .pfb forms,
#             and are under the respective licenses of the sources.
License:	Distributable

URL:		http://wiki.lyx.org/pmwiki.php/FAQ/Qt
Group:		System/Fonts/True type

Source0:	http://movementarian.org/latex-xft-fonts-%version.tar.gz

BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
Provides:	latex-xft-fonts
Requires(post):	chkfontpath
Requires(postun):chkfontpath
Requires(post):	fontconfig
Requires(postun):fontconfig

%description
This Package provides LaTeX TrueType fonts so that LyX can display LaTex
characters.

%prep
%setup -q -n latex-xft-fonts-%version

%build
perl -p -i -e "s|INSTALLDIR=.*|INSTALLDIR=%_datadir/fonts/TTF/latex|" Makefile

%install
rm -fr %buildroot
DESTDIR=%buildroot make install

(
cd %buildroot/%_datadir/fonts/TTF/latex/
# those are not unicode but in latex encoding
/usr/sbin/ttmkfdir -u | sed 's/iso10646-1/misc-fontspecific/' > fonts.scale
cp fonts.scale fonts.dir
)

%post
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/fonts/TTF/latex
touch %{_datadir}/fonts/TTF
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_sbindir/chkfontpath ] && \
   %_sbindir/chkfontpath -q -r %_datadir/fonts/TTF/latex
   [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc README
#
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/latex/
%_datadir/fonts/TTF/latex/*.ttf
#
%config(noreplace) %_datadir/fonts/TTF/latex/fonts.dir
%config(noreplace) %_datadir/fonts/TTF/latex/fonts.scale



