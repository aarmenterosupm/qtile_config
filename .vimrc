"  ________  ________  ________
" |\   __  \|\   __  \|\   ____\
" \ \  \|\  \ \  \|\  \ \  \___|	Asier Armenteros Cañibano
"  \ \   __  \ \   __  \ \  \		Custom VIM Config
"   \ \  \ \  \ \  \ \  \ \  \____
"    \ \__\ \__\ \__\ \__\ \_______\
"     \|__|\|__|\|__|\|__|\|_______|

" The following comments are the copyright and licensing information from the default
" qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
" 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
"
" Permission is hereby granted, free of charge, to any person obtaining a copy of this
" software and associated documentation files (the 'Software'), to deal in the Software
" without restriction, including without limitation the rights to use, copy, modify,
" merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
" permit persons to whom the Software is furnished to do so, subject to the following
" conditions:
"
" The above copyright notice and this permission notice shall be included in all copies
" or substantial portions of the Software.





" general stuff
syntax on
" syntax enable

set tabstop=4
set shiftwidth=4
set expandtab

set nu! " line numbers
set mouse=a

set nocompatible
filetype off " required
" filetype plugin on

"set cursorline
"set cursorcolumn
set encoding=utf-8
set t_Co=256

set laststatus=2
set noshowmode

set colorcolumn=80

" bells are evil!
set noerrorbells visualbell t_vb=

" tab navigation
map [1;5D <C-Left>
map [1;5C <C-Right>
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right>   :tabnext<CR>
nnoremap <C-t>     :tabnew<CR>
inoremap <C-Left> <Esc>:tabprevious<CR>i
inoremap <C-Right>   <Esc>:tabnext<CR>i
inoremap <C-t>     <Esc>:tabnew<CR>
map <C-w> :tabclose<CR>

" sane text paste
nnoremap <C-p> :set invpaste paste?<CR>
set pastetoggle=<C-p>

" Wrapped line navigation
nnoremap k gk
nnoremap j gj

" GUI
set go-=T
set go-=m
set go-=r
set go-=R
set go-=l
set go-=L


" Plugins
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle
" required!
Plugin 'gmarik/Vundle.vim'

" Plugins
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'

" do not open dir in new tab
" Plugin 'Nopik/vim-nerdtree-direnter'
" Plugin 'jistr/vim-nerdtree-tabs'
" Plugin 'Valloric/YouCompleteMe'
" Plugin 'ervandew/supertab'

Plugin 'flazz/vim-colorschemes'
Plugin 'w0rp/ale' "linter
Plugin 'spolu/dwm.vim'
Plugin 'tpope/vim-commentary'
Plugin 'tpope/vim-obsession'
Plugin 'godlygeek/tabular'
Plugin 'ntpeters/vim-better-whitespace'

" Plugin 'gcavallanti/vim-noscrollbar'

Plugin 'Raimondi/delimitMate'
Plugin 'Yggdroot/indentLine'
Plugin 'groenewege/vim-less'
Plugin 'christoomey/vim-tmux-navigator'
" Plugin 'tpope/vim-markdown'
Plugin 'reedes/vim-pencil'
" Plugin 'davidhalter/jedi-vim'
Plugin 'vim-scripts/indentpython.vim'
Plugin 'dhruvasagar/vim-table-mode'
Plugin 'rust-lang/rust.vim'
" Plugin 'vim-syntastic/syntastic'

" Plugin 'Shougo/neocomplete.vim'

call vundle#end()

filetype plugin indent on     " required!
syntax enable

" vim-colorschemes
colorscheme dracula
"colorscheme flattown

" Vim-latexsuite
" set grepprg=grep\ -nH\ $*
" let g:tex_flavor='latex'

" vim-pencil
" augroup pencil
    " autocmd!
    " autocmd FileType markdown,mkd call pencil#init()
    " autocmd FileType text call pencil#init()
" augroup END
let g:pencil#textwidth = 79
let g:airline_section_x = '%{PencilMode()}'
" let g:pencil#conceallevel = 0

" ALE
let g:airline#extensions#ale#enabled = 1
let g:ale_lint_on_text_changed = 'never'
" disable rustc execution
let g:ale_linters = {
\   'rust': [],
\}

" syntastic
" let g:syntastic_python_python_exec = 'python3'
" let g:syntastic_quiet_messages = { 'type': 'style' }
" let g:syntastic_python_checkers = ['pyflakes']

" let g:syntastic_mode_map = { 'mode': 'passive', 'active_filetypes': [],'passive_filetypes': [] }
" " nnoremap <C-w>E :SyntasticCheck<CR> :SyntasticToggleMode<CR>

" indentLine (show indentation)
let g:indentLine_char = '|'
let g:indentLine_color_term = 239

" NERDTree
map <C-y> :NERDTreeToggle<CR>

" Commentary
map <C-x> <Plug>CommentaryLine
vmap <C-x> <Plug>Commentary

" lightline.vim
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'component': {
      \   'readonly': '%{&readonly?"":""}',
      \ },
      \ 'separator': { 'left': '', 'right': '' },
      \ 'subseparator': { 'left': '', 'right': '' }
      \ }

" vim-markdown
" let g:markdown_fenced_languages = ['html', 'python', 'bash=sh']

" vim-table-mode
let g:table_mode_corner_corner = '+'
let g:table_mode_header_fillchar = '='

" tmux compatibility
map <Esc>[B <Down>

if &term =~ '256color'
" if &term =~ '^screen'
" disable Background Color Erase (BCE) so that color schemes
" render properly when inside 256-color tmux and GNU screen.
" see also http://snk.tuxfamily.org/log/vim-256color-bce.html
    set t_ut=
endif

" do not quote signature in mutt
au BufRead /tmp/mutt* normal :g/^> -- $/,/^$/-1d^M/^$^M^L
