import type { IUser } from '@/types/users';

export const Card = ({ user }: { user: IUser }) => {
        return (
            <div className="card">
                <h2>{user.firstName} {user.lastName}</h2>
                <p>Username: {user.username}</p>
                <p>Email: {user.email}</p>
            </div>
        );
    }

