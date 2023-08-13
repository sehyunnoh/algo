function solution(yl, yr, fl, fr) {
  return Math.max(yl, yr) === Math.max(fl, fr) && (yl+yr) === (fl+fr)
}