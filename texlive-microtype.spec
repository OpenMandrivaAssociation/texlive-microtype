%global tl_name microtype
%global tl_revision 78228

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.2d
Release:	%{tl_revision}.1
Summary:	Subliminal refinements towards typographical perfection
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/microtype
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a LaTeX interface to the micro-typographic
extensions that were introduced by pdfTeX and have since also propagated
to XeTeX and LuaTeX: most prominently, character protrusion and font
expansion, furthermore the adjustment of interword spacing and
additional kerning, as well as hyphenatable letterspacing (tracking) and
the possibility to disable all or selected ligatures. These features may
be applied to customisable sets of fonts, and all micro-typographic
aspects of the fonts can be configured in a straight-forward and
flexible way. Settings for various fonts are provided. Note that
character protrusion requires pdfTeX, LuaTeX, or XeTeX. Font expansion
works with pdfTeX or LuaTeX. The package will by default enable
protrusion and expansion if they can safely be assumed to work.
Disabling ligatures requires pdfTeX or LuaTeX, while the adjustment of
interword spacing and of kerning only works with pdfTeX. Letterspacing
is available with pdfTeX, LuaTeX or XeTeX. The alternative package
'letterspace', which also works with plain TeX, provides the user
commands for letterspacing only, omitting support for all other
extensions.

