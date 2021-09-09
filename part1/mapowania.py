def generate_pts_from_ranges(A):
  pts_tmp = []
  for e in A:
    pts_tmp.append(e[0])
    pts_tmp.append(e[1])

  pts_tmp.sort()

  pts = [pts_tmp[0]]
  for e in pts_tmp:
    if e != pts[-1]:
      pts.append(e)

  return pts


def generate_pts_from_points(A):
  A.sort()

  pts = [A[0]]
  for e in A:
    if e != A[-1]:
      pts.append(e)

  return pts


def map_pt(p, pts):
  n = len(pts)
  l = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if pts[c] < p:
      l = c + 1
    elif pts[c] > p:
      r = c - 1
    else:
      while c > 0 and pts[c-1] == p:
        c -= 1
      break

  if pts[c] != p:
    return None
  return c