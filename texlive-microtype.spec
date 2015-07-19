# revision 30755
# category Package
# catalog-ctan /macros/latex/contrib/microtype
# catalog-date 2013-05-26 21:18:14 +0200
# catalog-license lppl
# catalog-version 2.5a
Name:		texlive-microtype
Version:	2.5a
Release:	9
Summary:	Subliminal refinements towards typographical perfection
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/microtype
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.source.tar.xz
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
%{_texmfdistdir}/tex/latex/microtype/letterspace.sty
%{_texmfdistdir}/tex/latex/microtype/microtype-luatex.def
%{_texmfdistdir}/tex/latex/microtype/microtype-pdftex.def
%{_texmfdistdir}/tex/latex/microtype/microtype-xetex.def
%{_texmfdistdir}/tex/latex/microtype/microtype.cfg
%{_texmfdistdir}/tex/latex/microtype/microtype.lua
%{_texmfdistdir}/tex/latex/microtype/microtype.sty
%{_texmfdistdir}/tex/latex/microtype/mt-CharisSIL.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-LatinModernRoman.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-PalatinoLinotype.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-bch.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-blg.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-cmr.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-euf.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-eur.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-euroitc.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-eus.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-msa.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-msb.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-mvs.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-pad.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-pmn.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-ppl.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-ptm.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-ugm.cfg
%{_texmfdistdir}/tex/latex/microtype/mt-zpeu.cfg
%doc %{_texmfdistdir}/doc/latex/microtype/README
%doc %{_texmfdistdir}/doc/latex/microtype/microtype.pdf
%doc %{_texmfdistdir}/doc/latex/microtype/test-microtype.tex
#- source
%doc %{_texmfdistdir}/source/latex/microtype/microtype-utf.dtx
%doc %{_texmfdistdir}/source/latex/microtype/microtype.dtx
%doc %{_texmfdistdir}/source/latex/microtype/microtype.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
