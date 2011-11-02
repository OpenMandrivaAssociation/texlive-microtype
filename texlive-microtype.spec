Name:		texlive-microtype
Version:	2.4
Release:	1
Summary:	An interface to the micro-typographic features of pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/microtype
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a LaTeX interface to pdfTeX's micro-
typographic extensions: character protrusion and font
expansion. The package also offers a lua interface to the
corresponding features of LuaTeX. The package allows you to
restrict character protrusion and/or font expansion to a
certain set of fonts, or to certain parts of the document (for
example, based on selected language), and to configure micro-
typographic aspects of the fonts in a straight-forward and
flexible way. Settings for various fonts are provided. The
bundle also provides a letterspace package; this improves on
the alternatives (letterspacing and soul), and also provides a
means of protecting ligatures--notably those in fraktur fonts.
Note: Font expansion and character protrusion only work with
pdfTeX and LuaTeX. For pdfTeX, at least version 0.14f is
required; version 1.20a is needed for automatic font expansion.
With pdfTeX version 1.30, a command is provided for suppressing
ligatures.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/microtype/letterspace.sty
%{_texmfdistdir}/tex/latex/microtype/microtype.cfg
%{_texmfdistdir}/tex/latex/microtype/microtype.lua
%{_texmfdistdir}/tex/latex/microtype/microtype.sty
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
%doc %{_texmfdistdir}/source/latex/microtype/microtype.dtx
%doc %{_texmfdistdir}/source/latex/microtype/microtype.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
