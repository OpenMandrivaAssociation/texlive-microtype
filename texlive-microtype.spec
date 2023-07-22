Name:		texlive-microtype
Version:	66587
Release:	1
Summary:	Subliminal refinements towards typographical perfection
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/microtype
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LaTeX interface to the micro-typographic
extensions that were introduced by pdfTeX and have since also
propagated to XeTeX and LuaTeX: most prominently, character
protrusion and font expansion, furthermore the adjustment of
interword spacing and additional kerning, as well as
hyphenatable letterspacing (tracking) and the possibility to
disable all or selected ligatures. These features may be
applied to customisable sets of fonts, and all micro-
typographic aspects of the fonts can be configured in a
straight-forward and flexible way. Settings for various fonts
are provided. Note that character protrusion requires pdfTeX,
LuaTeX, or XeTeX. Font expansion works with pdfTeX or LuaTeX.
The package will by default enable protrusion and expansion if
they can safely be assumed to work. Disabling ligatures
requires pdfTeX or LuaTeX, while the adjustment of interword
spacing and of kerning only works with pdfTeX. Letterspacing is
available with pdfTeX or LuaTeX. The alternative package
`letterspace', which also works with plain TeX, provides the
user commands for letterspacing only, omitting support for all
other extensions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/microtype
%doc %{_texmfdistdir}/doc/latex/microtype
#- source
%doc %{_texmfdistdir}/source/latex/microtype

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
