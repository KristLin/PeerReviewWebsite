module.exports = {
    devServer: {
        proxy: {
            '/api': {
                // target: 'https://krist-9900-backend.herokuapp.com',
                target: 'http://localhost:8000',
                changeOrigin: true,
                pathRewrite: {'^/api' : ''}
            },
        }
    }
}