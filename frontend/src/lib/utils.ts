export const getHostname = (url: string) => {
    // use URL constructor and return hostname
    return new URL(url).hostname;
};

export const capitalizeFirstLetter = (string: string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
}