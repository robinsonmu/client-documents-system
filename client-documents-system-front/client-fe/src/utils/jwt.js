const utils = {
    parseJwt: function (token) {
        var base64Url = token.split(".")[1];
        var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
        var jsonPayload = decodeURIComponent(
            atob(base64)
                .split("")
                .map(function (c) {
                    return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
                })
                .join("")
        );

        return JSON.parse(jsonPayload);
    },
    getTokenExpTime: function (token) {
        let tokenObj = this.parseJwt(token)
        return tokenObj.exp;
    },

    tokenIsValid: function (token) {
        try {
            const tokenObj = this.parseJwt(token)
            const tokenTime = tokenObj.exp
            const difference = Math.floor(Date.now() / 1000) - tokenTime
            return difference <= 0
        } catch (error) {
            return false
        }
    }
}

export default utils;