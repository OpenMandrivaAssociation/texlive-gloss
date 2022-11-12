Name:		texlive-gloss
Version:	15878
Release:	1
Summary:	Create glossaries using BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gloss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A glossary package using BibTeX with \cite replaced by \gloss.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/gloss/glsbase.bib
%{_texmfdistdir}/bibtex/bib/gloss/sample.bib
%{_texmfdistdir}/bibtex/bst/gloss/glsplain.bst
%{_texmfdistdir}/bibtex/bst/gloss/glsshort.bst
%{_texmfdistdir}/tex/latex/gloss/gloss.sty
%doc %{_texmfdistdir}/doc/latex/gloss/README
%doc %{_texmfdistdir}/doc/latex/gloss/gloss.pdf
%doc %{_texmfdistdir}/doc/latex/gloss/gloss.tex
%doc %{_texmfdistdir}/doc/latex/gloss/sample.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
