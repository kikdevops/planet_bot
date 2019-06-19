FROM docker:dind

RUN apk add --no-cache bash \
  moreutils \
  nfs-utils \
  git \
  tzdata \ 
  cifs-utils \
  ansible \
  python \
  tree
