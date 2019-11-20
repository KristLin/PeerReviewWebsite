module.exports = {
    devServer: {
        proxy: {
            '/api': {
                // target: 'https://krist-9900-backend.herokuapp.com',
                target: 'http://localhost:5000',
                changeOrigin: true,
                pathRewrite: {'^/api' : ''}
            },
        }
    }
}