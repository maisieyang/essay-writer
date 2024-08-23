export default {
    async rewrites() {
      return [
        {
          source: '/api/:path*',
          destination: 'http://backend:5000/api/:path*', // 使用服务名作为目标地址
        },
      ];
    },
  };
  