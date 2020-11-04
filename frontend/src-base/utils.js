export const encodedObjectUrl = language => {
  return Object.entries(language)
    .map(([key, val]) => `${key}=${encodeURIComponent(val)}`)
    .join('&')
}
