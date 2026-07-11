%global tl_name gloss
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.2
Release:	%{tl_revision}.1
Summary:	Create glossaries using BibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gloss
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gloss.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A glossary package using BibTeX with \cite replaced by \gloss.

