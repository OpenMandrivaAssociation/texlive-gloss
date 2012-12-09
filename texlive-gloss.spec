# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gloss
# catalog-date 2006-12-11 14:57:52 +0100
# catalog-license lppl
# catalog-version 1.5.2
Name:		texlive-gloss
Version:	1.5.2
Release:	2
Summary:	Create glossaries using BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gloss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2-2
+ Revision: 752318
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2-1
+ Revision: 718559
- texlive-gloss
- texlive-gloss
- texlive-gloss
- texlive-gloss

